package model;

public class SensorResponse {
    private String operation = "";
    private String expression = "";
    private String result = "";
    private Sensor Sensor;

    public String getOperation() {
        return operation;
    }

    public void setOperation(String operation) {
        this.operation = operation;
    }

    public String getExpression() {
        return expression;
    }

    public void setExpression(String expression) {
        this.expression = expression;
    }

    public void setResult(String result) {
        this.result = result;
    }

    public String getResult() {
        return result;
    }

    public Sensor getSensor() {
        return Sensor;
    }

    public void setSensor(Sensor Sensor) {
        this.Sensor = Sensor;
    }
}
