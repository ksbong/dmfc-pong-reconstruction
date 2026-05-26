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