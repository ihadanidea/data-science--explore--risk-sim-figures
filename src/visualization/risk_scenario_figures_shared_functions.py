import pandas as pd

def data_loading_and_preparation(filepath):
    sim_df = pd.read_csv(filepath)

    sim_df["five_minute_marks"] = sim_df.index
    sim_df["minutes_post_simulation"] = sim_df["five_minute_marks"].apply(
        lambda x: x * 5
    )
    sim_df["hours_post_simulation"] = sim_df["minutes_post_simulation"] / 60

    sim_df["temp_basal_sbr_if_nan"] = sim_df["temp_basal"].mask(
        pd.isnull, sim_df["sbr"]
    )
    return sim_df


# TODO: have this function pull from design team tools api
# This is where the specific features are pulled from
def get_features_dictionary(field):
    if field == "bg":
        features_dictionary = dict(
            legend_label="rTBG Trace (True BG)",
            color="#B1BEFF",
            alpha=1.0,
            linestyle="None",
            linewidth=0,
            marker="o",
            markersize=3,
            drawstyle="default",
            mode="markers",
            dash=None,
            fill=None,
            shape="linear",
        )
    elif field == "bg_sensor":
        features_dictionary = dict(
            legend_label=" iCGM",
            color="#6AA84F",
            alpha=1.0,
            linestyle="None",
            linewidth=0,
            marker="o",
            markersize=3,
            drawstyle="default",
            mode="markers",
            dash="dash",
            fill=None,
            shape="linear",
        )
    elif field == "sbr":
        features_dictionary = dict(
            legend_label="Scheduled Basal Rate",
            color="black",
            alpha=1,
            linestyle="--",
            linewidth=2,
            marker="None",
            markersize=0,
            drawstyle="default",
            mode="lines",
            dash="dash",
            fill=None,
            shape="linear",
        )
    elif field == "iob":
        features_dictionary = dict(
            legend_label="Insulin On Board",
            color="#744AC2",
            alpha=1,
            linestyle="solid",
            linewidth=2,
            marker="None",
            markersize=0,
            drawstyle="default",
            mode="lines",
            dash=None,
            fill=None,
            shape="linear",
        )
    elif field == "temp_basal_sbr_if_nan":
        features_dictionary = dict(
            legend_label="Loop Decision",
            color="#008ECC",
            alpha=1,
            linestyle="solid",
            step="pre",
            drawstyle="steps-pre",
            linewidth=2,
            marker="o",
            markersize=2,
            mode="lines",
            dash=None,
            fill="tozeroy",
            shape="hv",
        )
    elif field == "delivered_basal_insulin":
        features_dictionary = dict(
            legend_label="Delivered Basal Insulin",
            color="#f9706b",
            alpha=0.4,
            linestyle="solid",
            linewidth=1,
            marker="o",
            markersize=2,
            drawstyle="default",
            mode="markers",
            dash="dash",
            fill=None,
            shape="linear",
        )

    # Todo: update with specific feature attributes want to use for fields below

    elif field == "undelivered_basal_insulin":
        features_dictionary = dict(
            legend_label="Undelivered Basal Insulin",
            color="#DB2E2C",
            alpha=1,
            linestyle="--",
            linewidth=2,
            marker="None",
            markersize=0,
            drawstyle="default",
        )
    elif field == "pump_sbr":
        features_dictionary = dict(
            legend_label="Pump Scheduled Basal Rate",
            color="#0068B5",
            alpha=1,
            linestyle="--",
            linewidth=2,
            marker="None",
            markersize=0,
            drawstyle="default",
        )
    elif field == "cir":
        features_dictionary = dict(
            legend_label="Carb-Insulin-Ratio",
            color="#f9706b",
            alpha=1.0,
            linestyle="None",
            linewidth=0,
            marker="o",
            markersize=8,
            drawstyle="default",
        )
    elif field == "pump_cir":
        features_dictionary = dict(
            legend_label="Pump Carb-Insulin-ratio",
            color="#40EBF9",
            alpha=1.0,
            linestyle="None",
            linewidth=0,
            marker="o",
            markersize=8,
            drawstyle="default",
        )
    elif field == "isf":
        features_dictionary = dict(
            legend_label="Insulin-Sensitivity-Factor",
            color="#f9706b",
            alpha=1.0,
            linestyle="None",
            linewidth=0,
            marker="o",
            markersize=8,
            drawstyle="default",
        )
    elif field == "pump_isf":
        features_dictionary = dict(
            legend_label="Pump Insulin-Sensitivity-Factor",
            color="#40EBF9",
            alpha=1.0,
            linestyle="None",
            linewidth=0,
            marker="o",
            markersize=8,
            drawstyle="default",
        )
    elif field == "reported_bolus":
        features_dictionary = dict(
            legend_label="Reported Bolus Value",
            color="#0068B5",
            alpha=1.0,
            linestyle="None",
            linewidth=0,
            marker="o",
            markersize=8,
            drawstyle="default",
        )
    elif field == "true_bolus":
        features_dictionary = dict(
            legend_label="True Bolus Value",
            color="#4ce791",
            alpha=1.0,
            linestyle="None",
            linewidth=0,
            marker="o",
            markersize=8,
            drawstyle="default",
        )
    elif field == "true_carb_value":
        features_dictionary = dict(
            legend_label="True Carb Value",
            color="#f95f3b",
            alpha=1.0,
            linestyle="None",
            linewidth=0,
            marker="o",
            markersize=8,
            drawstyle="default",
        )
    elif field == "reported_carb_value":
        features_dictionary = dict(
            legend_label="Reported Carb Value",
            color="#4ce791",
            alpha=1.0,
            linestyle="None",
            linewidth=0,
            marker="o",
            markersize=8,
            drawstyle="default",
        )
    elif field == "true_carb_duration":
        features_dictionary = dict(
            legend_label="True Carb Duration",
            color="#f9706b",
            alpha=1.0,
            linestyle="None",
            linewidth=0,
            marker="o",
            markersize=8,
            drawstyle="default",
        )
    elif field == "reported_carb_duration":
        features_dictionary = dict(
            legend_label="Reported Carb Duration",
            color="#40EBF9",
            alpha=1.0,
            linestyle="None",
            linewidth=0,
            marker="0",
            markersize=8,
            drawstyle="default",
        )
    return features_dictionary
