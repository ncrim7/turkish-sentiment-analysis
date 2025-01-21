def calculate_metrics(df):
    df["Duygu"] = df["Duygu"].str.capitalize()
    df["Tahmin"] = df["Tahmin"].str.capitalize()

    dp = len(df[(df["Duygu"] == "Pozitif") & (df["Tahmin"] == "Pozitif")])  # Doğru Pozitif
    yp = len(df[(df["Duygu"] == "Negatif") & (df["Tahmin"] == "Pozitif")])  # Yanlış Pozitif
    yn = len(df[(df["Duygu"] == "Pozitif") & (df["Tahmin"] == "Negatif")])  # Yanlış Negatif
    dn = len(df[(df["Duygu"] == "Negatif") & (df["Tahmin"] == "Negatif")])  # Doğru Negatif

    accuracy = (dp + dn) / len(df)
    precision = dp / (dp + yp) if (dp + yp) > 0 else 0
    recall = dp / (dp + yn) if (dp + yn) > 0 else 0
    f1 = (2 * precision * recall) / (precision + recall) if (precision + recall) > 0 else 0

    return {
        "Doğruluk (Accuracy)": accuracy,
        "Kesinlik (Precision)": precision,
        "Anma (Recall)": recall,
        "F1-Ölçütü": f1,
    }
