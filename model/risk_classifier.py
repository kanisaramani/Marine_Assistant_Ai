def classify_bleaching_risk(sst_anomaly):
    """
    Classifies coral bleaching risk based on SST anomaly value.
    """
    if sst_anomaly < 0.8:
        return "Low"
    elif sst_anomaly < 1.5:
        return "Moderate"
    else:
        return "High"
