package model;

public enum SensorType {
    TEMP("temp"),
    HUMIDITY("humidity"),
    CO2("CO2"),
    NO2("NO2"),
    WEIGHT("weight");

    private String type;

    SensorType(String type) {
        this.type = type;
    }

    public String getTypeString() {
        return type;
    }
}
