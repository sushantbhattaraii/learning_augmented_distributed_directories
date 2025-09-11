<<<<<<< HEAD
import pandas as pd
import glob
import matplotlib.pyplot as plt
import re
import numpy as np
import os
from matplotlib.patches import Patch

# Gather and sort all Excel files
files = sorted(glob.glob('./results/conceptone_data/random/128nodes_diameter104_cutoff2.5*.xlsx'))

# Extract node count and overlap from filename
m = re.search(r'(\d+)nodes_', files[0])
node_count = m.group(1) if m else "?"

m2 = re.search(r'overlap(\d+)', files[0])
overlap_value = m2.group(1) if m2 else "?"

# Prepare colormap
cmap = plt.get_cmap('tab20')

# Collect all distinct fractions across files
all_fractions = set()
for f in files:
    df_tmp = pd.read_excel(f)
    all_fractions.update(df_tmp['fraction'].unique())

fractions_sorted = sorted(all_fractions)
x_positions = np.arange(len(fractions_sorted))

# Create subplots: one for error, one for stretch/arrow
fig, (ax1, ax3) = plt.subplots(1, 2, figsize=(14, 11), sharex=False)

n_files = len(files)
cluster_gap = 0.7     # horizontal spacing between clusters of different cutoffs
series_sep = 0.22     # separation between PArrow and Arrow within a cutoff
box_width = 0.18      # box width

# Loop over files (cutoffs)
for idx, f in enumerate(files):
    df = pd.read_excel(f)

    # ----- Error line plot (keep as before) -----
    mean_max_error = df.groupby('fraction')['max_error'].mean()
    cutoff = f.split("_cutoff")[1].split("-")[0]
    actual_cutoff = 1 / float(cutoff)

    ax1.plot(
        mean_max_error.index,
        mean_max_error.values,
        marker='o',
        label=f'Prediction Error ≤ {actual_cutoff}',
        color=cmap(2 * idx)
    )

    # ----- Stretch & Arrow boxplots -----
    stretch_groups = []
    arrow_groups = []
    for fr in fractions_sorted:
        stretch_groups.append(df.loc[df['fraction'] == fr, 'stretch'].values)
        arrow_groups.append(df.loc[df['fraction'] == fr, 'stretch_arrow'].values)

    # Spread cutoffs symmetrically around cluster centers
    if n_files == 1:
        cutoff_offset = 0.0
    else:
        cutoff_offset = (idx - (n_files - 1) / 2) * (cluster_gap / max(n_files - 1, 1))

    # Positions for PArrow and Arrow
    pos_parrow = x_positions + cutoff_offset - series_sep / 2
    pos_arrow = x_positions + cutoff_offset + series_sep / 2

    # Create boxplots
    bp_parrow = ax3.boxplot(
        stretch_groups,
        positions=pos_parrow,
        widths=box_width,
        patch_artist=True,
        manage_ticks=False
    )
    bp_arrow = ax3.boxplot(
        arrow_groups,
        positions=pos_arrow,
        widths=box_width,
        patch_artist=True,
        manage_ticks=False
    )

    # Color them
    parrow_face = cmap(2 * idx + 1)
    arrow_face = cmap(2 * idx + 2)
    for patch in bp_parrow['boxes']:
        patch.set_facecolor(parrow_face); patch.set_alpha(0.55)
    for patch in bp_arrow['boxes']:
        patch.set_facecolor(arrow_face); patch.set_alpha(0.55)

    # Make whiskers/medians a bit thinner
    for part in ['whiskers', 'caps', 'medians']:
        for line in bp_parrow[part] + bp_arrow[part]:
            line.set_linewidth(1.2)

# ---- Formatting ----
# Error subplot
ax1.set_ylabel('Error')
ax1.set_xlabel('Number of operations')
ax1.set_title('Error vs Number of operations')
ax1.legend(loc='best')

# Stretch subplot
ax3.set_ylabel('PArrow and Arrow Stretch')
ax3.set_xlabel('Number of operations')
ax3.set_title('PArrow & Arrow Stretch vs Number of operations')
ax3.set_xticks(x_positions)
ax3.set_xticklabels([str(fr) for fr in fractions_sorted])

# Add a generic legend for box colors
handles = [
    Patch(facecolor='gray', alpha=0.55, label='PArrow'),
    Patch(facecolor='lightblue', alpha=0.55, label='Arrow')
]
ax3.legend(handles=handles, loc='best')

# Save or display
plt.tight_layout()
folder = "conceptone_plots"
folder2 = "random"
filename = f'{node_count}_nodes_boxplots.png'
path_to_save = os.path.join('results', folder, folder2, filename)

# plt.savefig(path_to_save)
plt.show()
=======
import pandas as pd
import glob
import matplotlib.pyplot as plt
import re
import numpy as np
import os
from matplotlib.patches import Patch

# Gather and sort all Excel files
files = sorted(glob.glob('./results/conceptone_data/random/128nodes_diameter104_cutoff2.5*.xlsx'))

# Extract node count and overlap from filename
m = re.search(r'(\d+)nodes_', files[0])
node_count = m.group(1) if m else "?"

m2 = re.search(r'overlap(\d+)', files[0])
overlap_value = m2.group(1) if m2 else "?"

# Prepare colormap
cmap = plt.get_cmap('tab20')

# Collect all distinct fractions across files
all_fractions = set()
for f in files:
    df_tmp = pd.read_excel(f)
    all_fractions.update(df_tmp['fraction'].unique())

fractions_sorted = sorted(all_fractions)
x_positions = np.arange(len(fractions_sorted))

# Create subplots: one for error, one for stretch/arrow
fig, (ax1, ax3) = plt.subplots(1, 2, figsize=(14, 11), sharex=False)

n_files = len(files)
cluster_gap = 0.7     # horizontal spacing between clusters of different cutoffs
series_sep = 0.22     # separation between PArrow and Arrow within a cutoff
box_width = 0.18      # box width

# Loop over files (cutoffs)
for idx, f in enumerate(files):
    df = pd.read_excel(f)

    # ----- Error line plot (keep as before) -----
    mean_max_error = df.groupby('fraction')['max_error'].mean()
    cutoff = f.split("_cutoff")[1].split("-")[0]
    actual_cutoff = 1 / float(cutoff)

    ax1.plot(
        mean_max_error.index,
        mean_max_error.values,
        marker='o',
        label=f'Prediction Error ≤ {actual_cutoff}',
        color=cmap(2 * idx)
    )

    # ----- Stretch & Arrow boxplots -----
    stretch_groups = []
    arrow_groups = []
    for fr in fractions_sorted:
        stretch_groups.append(df.loc[df['fraction'] == fr, 'stretch'].values)
        arrow_groups.append(df.loc[df['fraction'] == fr, 'stretch_arrow'].values)

    # Spread cutoffs symmetrically around cluster centers
    if n_files == 1:
        cutoff_offset = 0.0
    else:
        cutoff_offset = (idx - (n_files - 1) / 2) * (cluster_gap / max(n_files - 1, 1))

    # Positions for PArrow and Arrow
    pos_parrow = x_positions + cutoff_offset - series_sep / 2
    pos_arrow = x_positions + cutoff_offset + series_sep / 2

    # Create boxplots
    bp_parrow = ax3.boxplot(
        stretch_groups,
        positions=pos_parrow,
        widths=box_width,
        patch_artist=True,
        manage_ticks=False
    )
    bp_arrow = ax3.boxplot(
        arrow_groups,
        positions=pos_arrow,
        widths=box_width,
        patch_artist=True,
        manage_ticks=False
    )

    # Color them
    parrow_face = cmap(2 * idx + 1)
    arrow_face = cmap(2 * idx + 2)
    for patch in bp_parrow['boxes']:
        patch.set_facecolor(parrow_face); patch.set_alpha(0.55)
    for patch in bp_arrow['boxes']:
        patch.set_facecolor(arrow_face); patch.set_alpha(0.55)

    # Make whiskers/medians a bit thinner
    for part in ['whiskers', 'caps', 'medians']:
        for line in bp_parrow[part] + bp_arrow[part]:
            line.set_linewidth(1.2)

# ---- Formatting ----
# Error subplot
ax1.set_ylabel('Error')
ax1.set_xlabel('Number of operations')
ax1.set_title('Error vs Number of operations')
ax1.legend(loc='best')

# Stretch subplot
ax3.set_ylabel('PArrow and Arrow Stretch')
ax3.set_xlabel('Number of operations')
ax3.set_title('PArrow & Arrow Stretch vs Number of operations')
ax3.set_xticks(x_positions)
ax3.set_xticklabels([str(fr) for fr in fractions_sorted])

# Add a generic legend for box colors
handles = [
    Patch(facecolor='gray', alpha=0.55, label='PArrow'),
    Patch(facecolor='lightblue', alpha=0.55, label='Arrow')
]
ax3.legend(handles=handles, loc='best')

# Save or display
plt.tight_layout()
folder = "conceptone_plots"
folder2 = "random"
filename = f'{node_count}_nodes_boxplots.png'
path_to_save = os.path.join('results', folder, folder2, filename)

# plt.savefig(path_to_save)
plt.show()
>>>>>>> 836df541228e314a5a6d824d46aca2c43a5f286f
