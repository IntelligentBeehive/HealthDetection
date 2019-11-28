package service;

import com.google.gson.Gson;
import com.google.gson.reflect.TypeToken;
import database.Database;
import model.*;

import javax.ws.rs.*;
import javax.ws.rs.core.Context;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;
import javax.ws.rs.core.UriInfo;
import java.lang.reflect.Type;
import java.net.MalformedURLException;
import java.util.Map;

@Path("/sensors")
public class SensorService {

    private Gson gson = new Gson();
    private Database database = new Database();

    // TODO: Basic Auth
    // TODO: add getByTypeBetween(time x, time y)

    @GET
    @Path("/{type}")
    @Produces(MediaType.APPLICATION_JSON)
    public Response getAllByType(
            @Context UriInfo uriInfo,
            @PathParam("type") String type,
            @QueryParam("timeFrom") String timeFrom,
            @QueryParam("timeTo") String timeTo
    ) {
        SensorResponseList response = new SensorResponseList();
        response.setOperation("getAllByType");
        response.setExpression("/" + type);
        try {
            type = type.toUpperCase();
            var sensorType = SensorType.valueOf(type);

            boolean between = !isNullOrEmpty(timeFrom) && !isNullOrEmpty(timeTo);
            var sensorMap = between ? database.getAllByTypeBetween(sensorType, timeFrom, timeTo) : database.getAllByType(sensorType);
            var url = uriInfo.getBaseUri().toURL().toString();

            for (Sensor p : sensorMap.values()) {
                p.setUrl(url);
                response.addToResponseList(p);
            }
            if(response.getSensorList().size() < 1) {
                throw new Exception("No results found");
            }

            response.setResult("success");


        } catch (Exception e) {
            response.setResult("invalid value");
            e.printStackTrace();

            return Response.status(400).entity(response).build();
        }

        String output = gson.toJson(response);
        return Response.status(200).entity(output).build();
    }


    @GET
    @Path("/{type}/{id}")
    @Produces(MediaType.APPLICATION_JSON)
    public Response getSensor(@PathParam("type") String type, @PathParam("id") String id) {

        SensorResponse response = new SensorResponse();
        response.setOperation("getSensor");
        response.setExpression("/" + type + "/" + id);

        try {
            type = type.toUpperCase();
            var sensorType = SensorType.valueOf(type);
            var sensorId = Integer.parseInt(id);
            var sensor = database.getSensorById(sensorType, sensorId);

            if (sensor == null) {
                response.setResult("Sensor not found");
            } else {
                response.setResult("Sensor found");
                response.setSensor(sensor);
            }

        } catch (NumberFormatException nfe) {
            response.setResult("invalid value");
        }

        String output = gson.toJson(response);
        return Response.status(200).entity(output).build();
    }

    @POST
    @Consumes(MediaType.APPLICATION_JSON)
    @Produces(MediaType.APPLICATION_JSON)
    public Response insertSensor(
            String SensorInput
    ) {
        Type type = new TypeToken<SensorRequest>() {
        }.getType();
        SensorRequest request = gson.fromJson(SensorInput, type);

        SensorResponse response = new SensorResponse();
        response.setOperation("insertSensor");
        response.setExpression("POST");

        try {
            var stringRequestType = request.getType().toUpperCase();
            var requestType = SensorType.valueOf(stringRequestType);
            var requestValue = request.getValue();
            var sensor = new Sensor(requestType, requestValue);

            if (database.insertSensor(sensor) == 0) {
                response.setResult("invalid request");
                return Response.status(400).entity(response).build();
            }

            response.setResult("success");
            response.setSensor(sensor);

        } catch (NumberFormatException nfe) {
            response.setResult("invalid value");
            return Response.status(400).entity(response).build();
        }

        String output = gson.toJson(response);
        return Response.status(200).entity(output).build();
    }

    private static boolean isNullOrEmpty(String str) {
        return str == null || str.trim().isEmpty();
    }
}
