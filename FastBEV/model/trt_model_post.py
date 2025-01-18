import torch.nn as nn

class TRTModelPost(nn.Module):
    def __init__(self, model):
        super().__init__()
        self.neck_3d = model.neck_3d
        self.bbox_head = model.bbox_head

    def forward(self, mlvl_volumes):
        neck_3d_feature = self.neck_3d(mlvl_volumes)
        cls_scores, bbox_preds, dir_cls_preds = self.bbox_head(neck_3d_feature)

        cls_score = cls_scores[0].sigmoid()
        bbox_pred = bbox_preds[0]
        dir_cls_pred = dir_cls_preds[0].permute(0, 2, 3, 1).reshape(-1, 2)

        return cls_score, bbox_pred, dir_cls_pred
