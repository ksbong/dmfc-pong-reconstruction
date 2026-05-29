import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import rankdata

def draw_fig2c_neural_response_vis_epoch(dmfc, neuron_no, neuron_id, ax=None):
    created_fig = False

    if ax is None:
        fig, ax = plt.subplots(figsize=(4, 3))
        created_fig = True

    single_neuron = dmfc["neural_responses_reliable"]["occ"][neuron_no]

    t_from_start = dmfc["behavioral_responses"]["occ"]["t_from_start"]
    t_from_occ = dmfc["behavioral_responses"]["occ"]["t_from_occ"]

    mask = (
        np.isfinite(t_from_start)
        & np.isfinite(t_from_occ)
        & (t_from_start >= 0)
        & (t_from_occ <= 0)
    )

    time = np.arange(single_neuron.shape[1]) * 50

    yf = dmfc["meta"]["yf"]
    cax = rankdata(yf)
    cax = (cax - np.nanmin(cax)) / (np.nanmax(cax) - np.nanmin(cax))
    colors = plt.cm.plasma(cax)

    for i, response in enumerate(single_neuron):
        m = mask[i].astype(bool)
        response_masked = np.where(m, response, np.nan)
        valid_values = response_masked[np.isfinite(response_masked)]

        if len(valid_values) == 0:
            continue

        y_draw = np.full_like(response_masked, np.nan, dtype=float)
        y_draw[:len(valid_values)] = valid_values

        x_draw = time

        valid_idx = np.where(np.isfinite(y_draw))[0]
        first = valid_idx[0]
        last = valid_idx[-1]

        color = colors[i]

        ax.plot(
            x_draw,
            y_draw,
            color=color,
            alpha=0.85,
            linewidth=1.0,
        )

        ax.plot(
            x_draw[first],
            y_draw[first],
            marker="o",
            markersize=4,
            markerfacecolor="white",
            markeredgecolor=color,
            markeredgewidth=0.8,
            linestyle="None",
            zorder=5,
        )

        ax.plot(
            x_draw[last],
            y_draw[last],
            marker="o",
            markersize=4,
            markerfacecolor="white",
            markeredgecolor=color,
            markeredgewidth=0.8,
            linestyle="None",
            zorder=5,
        )

    ylim_mask = dmfc["masks"]["occ"]["start_end_pad0"]
    y_for_ylim = np.where(ylim_mask.astype(bool), single_neuron, np.nan)

    mm = np.nanmin(y_for_ylim)
    MM = np.nanmax(y_for_ylim)
    dr = MM - mm

    ax.set_ylim(mm - dr * 0.1, MM + dr * 0.1)
    ax.set_xlim(-50, 2000)
    ax.set_title(f"{neuron_id} - vis")

    if created_fig:
        plt.show()

    return ax

def draw_fig2c_neural_response_occ_epoch(dmfc, neuron_no, neuron_id, ax=None):
    created_fig = False

    if ax is None:
        fig, ax = plt.subplots(figsize=(4, 3))
        created_fig = True

    single_neuron = dmfc["neural_responses_reliable"]["occ"][neuron_no]

    t_from_occ = dmfc["behavioral_responses"]["occ"]["t_from_occ"]
    t_from_end = dmfc["behavioral_responses"]["occ"]["t_from_end"]

    mask = (
        np.isfinite(t_from_occ)
        & np.isfinite(t_from_end)
        & (t_from_occ >= 0)
        & (t_from_end <= 0)
    )

    time = np.arange(single_neuron.shape[1]) * 50

    yf = dmfc["meta"]["yf"]
    cax = rankdata(yf)
    cax = (cax - np.nanmin(cax)) / (np.nanmax(cax) - np.nanmin(cax))
    colors = plt.cm.plasma(cax)

    for i, response in enumerate(single_neuron):
        m = mask[i].astype(bool)
        response_masked = np.where(m, response, np.nan)
        valid_values = response_masked[np.isfinite(response_masked)]

        if len(valid_values) == 0:
            continue

        y_draw = np.full_like(response_masked, np.nan, dtype=float)
        y_draw[:len(valid_values)] = valid_values

        x_draw = time

        valid_idx = np.where(np.isfinite(y_draw))[0]
        first = valid_idx[0]
        last = valid_idx[-1]

        color = colors[i]

        ax.plot(
            x_draw,
            y_draw,
            color=color,
            alpha=0.85,
            linewidth=1.0,
        )

        ax.plot(
            x_draw[first],
            y_draw[first],
            marker="o",
            markersize=4,
            markerfacecolor="white",
            markeredgecolor=color,
            markeredgewidth=0.8,
            linestyle="None",
            zorder=5,
        )

        ax.plot(
            x_draw[last],
            y_draw[last],
            marker="o",
            markersize=4,
            markerfacecolor="white",
            markeredgecolor=color,
            markeredgewidth=0.8,
            linestyle="None",
            zorder=5,
        )

    ylim_mask = dmfc["masks"]["occ"]["start_end_pad0"]
    y_for_ylim = np.where(ylim_mask.astype(bool), single_neuron, np.nan)

    mm = np.nanmin(y_for_ylim)
    MM = np.nanmax(y_for_ylim)
    dr = MM - mm

    ax.set_ylim(mm - dr * 0.1, MM + dr * 0.1)
    ax.set_xlim(-50, 2000)
    ax.set_title(f"{neuron_id} - occ")

    if created_fig:
        plt.show()

    return ax


def draw_fig2c_spatial_modulation(
    dmfc,
    neuron_no,
    neuron_id,
    ax=None,
    bins=40,
    min_count=1,
    cmap="viridis",
):
    import numpy as np
    import matplotlib.pyplot as plt

    created_fig = False
    if ax is None:
        fig, ax = plt.subplots(figsize=(3, 3))
        created_fig = True

    single_neuron = dmfc["neural_responses_reliable"]["occ"][neuron_no]
    bh = dmfc["behavioral_responses"]["occ"]

    # Figure 1C matching 때처럼 plot coordinate는 보통 ball_pos 쪽이 더 직접적
    x = np.asarray(bh["ball_pos_x"], dtype=float)
    y = np.asarray(bh["ball_pos_y"], dtype=float)

    if "start_end_pad0" in dmfc["masks"]["occ"]:
        mask = dmfc["masks"]["occ"]["start_end_pad0"].astype(bool)
    else:
        mask = np.isfinite(x) & np.isfinite(y)

    valid = (
        mask
        & np.isfinite(x)
        & np.isfinite(y)
        & np.isfinite(single_neuron)
        & (x >= -10)
        & (x <= 10)
        & (y >= -10)
        & (y <= 10)
    )

    x_flat = x[valid]
    y_flat = y[valid]
    r_flat = single_neuron[valid]

    x_edges = np.linspace(-10, 10, bins + 1)
    y_edges = np.linspace(-10, 10, bins + 1)

    resp_sum, _, _ = np.histogram2d(
        y_flat,
        x_flat,
        bins=[y_edges, x_edges],
        weights=r_flat,
    )

    count, _, _ = np.histogram2d(
        y_flat,
        x_flat,
        bins=[y_edges, x_edges],
    )

    heat = resp_sum / np.maximum(count, 1)
    heat[count < min_count] = np.nan

    im = ax.imshow(
        heat,
        origin="lower",
        extent=[-10, 10, -10, 10],
        aspect="equal",
        cmap=cmap,
        interpolation="nearest",
    )

    # occluder boundary 대략 표시
    ax.axvline(5.625, color="black", linewidth=1.2)

    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    ax.set_title(f"{neuron_id} - spatial")
    ax.set_xlabel("x position (°)")
    ax.set_ylabel("y position (°)")

    if created_fig:
        plt.colorbar(im, ax=ax, fraction=0.046, pad=0.04)
        plt.show()

    return im

def draw_fig2c_example_row(dmfc, neuron_no, neuron_id=None, axes=None):
    """
    Draw one Fig. 2C-style row:
    visible response / occluded response / spatial modulation.
    """

    if neuron_id is None:
        neuron_id = neuron_no

    created_fig = False

    if axes is None:
        fig, axes = plt.subplots(1, 3, figsize=(9, 3))
        created_fig = True

    draw_fig2c_neural_response_vis_epoch(
        dmfc=dmfc,
        neuron_no=neuron_no,
        neuron_id=neuron_id,
        ax=axes[0],
    )

    draw_fig2c_neural_response_occ_epoch(
        dmfc=dmfc,
        neuron_no=neuron_no,
        neuron_id=neuron_id,
        ax=axes[1],
    )

    im = draw_fig2c_spatial_modulation(
        dmfc=dmfc,
        neuron_no=neuron_no,
        neuron_id=neuron_id,
        ax=axes[2],
    )

    if created_fig:
        plt.tight_layout()
        plt.show()

    return axes, im