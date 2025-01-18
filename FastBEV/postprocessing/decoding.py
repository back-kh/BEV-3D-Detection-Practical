import torch

def decode(anchors, deltas):
    xa, ya, za, wa, la, ha, ra, *cas = torch.split(anchors, 1, dim=-1)
    xt, yt, zt, wt, lt, ht, rt, *cts = torch.split(deltas, 1, dim=-1)

    diagonal = torch.sqrt(la**2 + wa**2)
    xg = xt * diagonal + xa
    yg = yt * diagonal + ya
    zg = zt * ha + za + ha / 2

    lg = torch.exp(lt) * la
    wg = torch.exp(wt) * wa
    hg = torch.exp(ht) * ha
    rg = rt + ra

    return torch.cat([xg, yg, zg, wg, lg, hg, rg], dim=-1)
