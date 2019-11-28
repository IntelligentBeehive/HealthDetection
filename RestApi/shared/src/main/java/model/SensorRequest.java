package model;

public class SensorRequest {

    private String type;
    private float value;

    public float getValue() {
        return this.value;
    }

    public String getType() {
        return this.type;
    }

    public SensorRequest() { }

    public SensorRequest(String type, float value) {
        this.type = type;
        this.value = value;
    }
}
