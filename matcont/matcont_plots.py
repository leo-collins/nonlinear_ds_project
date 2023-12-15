import matplotlib.pyplot as plt
import numpy as np
from scipy.io import loadmat

origin_branch = loadmat("origin_branch.mat")
limit_cycle_from_hopf = loadmat("limit_cycle_from_hopf_origin.mat")
first_period_doubling = loadmat("first_period_doubling.mat")
second_period_doubling = loadmat("second_period_doubling.mat")
third_period_doubling = loadmat("third_period_doubling.mat")
fourth_period_doubling = loadmat("fourth_period_doubling.mat")
fifth_period_doubling = loadmat("fifth_period_doubling.mat")

origin_branch_x_stable = origin_branch["x"][0][:5]
origin_branch_x_unstable = origin_branch["x"][0][5:13]
origin_branch_A_stable = origin_branch["x"][3][:5]
origin_branch_A_unstable = origin_branch["x"][3][5:13]

limit_cycle_max_x_stable = np.max(limit_cycle_from_hopf["x"][:-2:3], axis=0)[:720]
limit_cycle_max_x_unstable = np.max(limit_cycle_from_hopf["x"][:-2:3], axis=0)[720:]
limit_cycle_A_stable = limit_cycle_from_hopf["x"][-1][:720]
limit_cycle_A_unstable = limit_cycle_from_hopf["x"][-1][720:]

first_period_doubling_max_x_stable = np.max(first_period_doubling["x"][:-2:3], axis=0)[
    :197
]
first_period_doubling_max_x_unstable = np.max(
    first_period_doubling["x"][:-2:3], axis=0
)[197:]
first_period_doubling_A_stable = first_period_doubling["x"][-1][:197]
first_period_doubling_A_unstable = first_period_doubling["x"][-1][197:]

second_period_doubling_max_x_stable = np.max(
    second_period_doubling["x"][:-2:3], axis=0
)[:95]
second_period_doubling_max_x_unstable = np.max(
    second_period_doubling["x"][:-2:3], axis=0
)[95:]
second_period_doubling_A_stable = second_period_doubling["x"][-1][:95]
second_period_doubling_A_unstable = second_period_doubling["x"][-1][95:]

third_period_doubling_max_x_stable = np.max(third_period_doubling["x"][:-2:3], axis=0)[
    :45
]
third_period_doubling_max_x_unstable = np.max(
    third_period_doubling["x"][:-2:3], axis=0
)[45:]
third_period_doubling_A_stable = third_period_doubling["x"][-1][:45]
third_period_doubling_A_unstable = third_period_doubling["x"][-1][45:]

fourth_period_doubling_max_x_stable = np.max(
    fourth_period_doubling["x"][:-2:3], axis=0
)[:38]
fourth_period_doubling_max_x_unstable = np.max(
    fourth_period_doubling["x"][:-2:3], axis=0
)[38:]
fourth_period_doubling_A_stable = fourth_period_doubling["x"][-1][:38]
fourth_period_doubling_A_unstable = fourth_period_doubling["x"][-1][38:]

fifth_period_doubling_max_x_stable = np.max(fifth_period_doubling["x"][:-2:3], axis=0)[
    :13
]
fifth_period_doubling_max_x_unstable = np.max(
    fifth_period_doubling["x"][:-2:3], axis=0
)[13:]
fifth_period_doubling_A_stable = fifth_period_doubling["x"][-1][:13]
fifth_period_doubling_A_unstable = fifth_period_doubling["x"][-1][13:]

fig, ax = plt.subplots()

ax.plot(
    origin_branch_A_stable,
    origin_branch_x_stable,
    linestyle="solid",
    c="black",
    zorder=0,
)
ax.plot(
    origin_branch_A_unstable,
    origin_branch_x_unstable,
    linestyle="dashed",
    c="black",
    zorder=1,
)
ax.plot(
    limit_cycle_A_stable,
    limit_cycle_max_x_stable,
    linestyle="solid",
    c="green",
    zorder=2,
)
ax.plot(
    limit_cycle_A_unstable,
    limit_cycle_max_x_unstable,
    linestyle="dashed",
    c="green",
    zorder=3,
)
ax.plot(
    first_period_doubling_A_stable,
    first_period_doubling_max_x_stable,
    linestyle="solid",
    c="blue",
    zorder=4,
)
ax.plot(
    first_period_doubling_A_unstable,
    first_period_doubling_max_x_unstable,
    linestyle="dashed",
    c="blue",
    zorder=5,
)
ax.plot(
    second_period_doubling_A_stable,
    second_period_doubling_max_x_stable,
    linestyle="solid",
    c="red",
    zorder=6,
)
ax.plot(
    second_period_doubling_A_unstable,
    second_period_doubling_max_x_unstable,
    linestyle="dashed",
    c="red",
    zorder=7,
)
ax.plot(
    third_period_doubling_A_stable,
    third_period_doubling_max_x_stable,
    linestyle="solid",
    c="green",
    zorder=8,
)
ax.plot(
    third_period_doubling_A_unstable,
    third_period_doubling_max_x_unstable,
    linestyle="dashed",
    c="green",
    zorder=9,
)
# plt.plot(
#     fourth_period_doubling_A_stable,
#     fourth_period_doubling_max_x_stable,
#     linestyle="solid",
#     c="blue",
#     zorder=10,
# )
# plt.plot(
#     fourth_period_doubling_A_unstable,
#     fourth_period_doubling_max_x_unstable,
#     linestyle="dashed",
#     c="blue",
#     zorder=11,
# )
ax.plot(
    fifth_period_doubling_A_stable,
    fifth_period_doubling_max_x_stable,
    linestyle="solid",
    c="blue",
    zorder=12,
)
ax.plot(
    fifth_period_doubling_A_unstable,
    fifth_period_doubling_max_x_unstable,
    linestyle="dashed",
    c="blue",
    zorder=13,
)
ax.scatter([0.0595], [0], c="black", zorder=14, s=20)
ax.scatter([0.2301], [5.78414], c="black", zorder=15, s=20)
ax.scatter([0.26749154], [6.68178963], c="black", zorder=16, s=20)
ax.scatter([0.27599168], [6.87807003], c="black", zorder=17, s=20)
ax.scatter([0.27780535], [6.91586456], c="black", zorder=17, s=20)
ax.text(0.03, 0.3, "AH")
ax.text(0.2, 6, "PD")
ax.text(0.25, 7, "PD")
# ax.text(0.2755, 6.88, "PD")
# ax.text(0.2774, 6.92, "PD")
# ax.set_ylim(6.75, 7)
# ax.set_xlim([0.27, 0.28])
ax.set_xlabel(r"$a$")
ax.set_ylabel(r"max $x$")
plt.tight_layout()
plt.show()
