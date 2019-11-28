package model;

import java.security.Timestamp;

public class Sensor {
    private Integer id;
    private SensorType type;
    private float value;
    private String dateCreated;
    private String url;

    public Sensor() { } // Default to allow JSON Type convert

    public Sensor(SensorType type, float value) {
        this.type = type;
        this.value = value;
    }

    public Sensor(int id, SensorType type, float value, String dateCreated) {
        this.id = id;
        this.type = type;
        this.value = value;
        this.dateCreated = dateCreated;
    }

    public void setUrl(String baseUrl){
        this.url = baseUrl+"sensors/"+this.type.toString().toLowerCase()+"/"+this.id;
    }

    public int getId() {
        return id;
    }

    public String getUrl() {
        return url;
    }

    public float getValue() {
        return value;
    }

    public SensorType getType() {
        return type;
    }

    @Override
    public String toString() {
        return String.format("Type: %s, Value: %s Url: %s", type, value, url);
    }

    public String getDateCreated() {
        return dateCreated;
    }
}
