import torch.nn as nn
import torch.nn.functional as F

class TRTModelPre(nn.Module):
    def __init__(self, backbone, neck, multi_scale_id, n_voxels, neck_fuse_0):
        super().__init__()
        self.backbone = backbone
        self.neck = neck
        self.multi_scale_id = multi_scale_id
        self.n_voxels = n_voxels
        self.neck_fuse_0 = neck_fuse_0

    def forward(self, img):
        x = self.backbone(img)
        mlvl_feats = self.neck(x)

        if self.multi_scale_id:
            mlvl_feats = self._fuse_features(mlvl_feats)
        if isinstance(self.n_voxels, list):
            mlvl_feats = self._pad_features(mlvl_feats)

        assert len(mlvl_feats) == 1, "Only single-layer features supported!"
        return mlvl_feats[0]

    def _fuse_features(self, mlvl_feats):
        fused_feats = []
        for msid in self.multi_scale_id:
            fuse_feats = [mlvl_feats[msid]]
            for i in range(msid + 1, len(mlvl_feats)):
                resized_feat = F.interpolate(
                    mlvl_feats[i], size=mlvl_feats[msid].size()[2:], mode="bilinear", align_corners=False
                )
                fuse_feats.append(resized_feat)
            fused_feats.append(torch.cat(fuse_feats, dim=1))
        return fused_feats

    def _pad_features(self, mlvl_feats):
        pad_feats = len(self.n_voxels) - len(mlvl_feats)
        for _ in range(pad_feats):
            mlvl_feats.append(mlvl_feats[0])
        return mlvl_feats
