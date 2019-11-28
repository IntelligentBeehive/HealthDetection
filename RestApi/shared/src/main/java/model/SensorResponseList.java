package model;

import java.util.ArrayList;
import java.util.List;

public class SensorResponseList {
    private String operation = "";
    private String expression = "";
    private String result = "";
    private List<Sensor> SensorList = new ArrayList<>();

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

    public List<Sensor> getSensorList() {
        return SensorList;
    }

    public void setSensorList(List<Sensor> SensorList) {
        this.SensorList = SensorList;
    }

    public void addToResponseList(Sensor Sensor) {
        this.SensorList.add(Sensor);
    }
}
