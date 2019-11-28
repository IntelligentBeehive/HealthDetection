package database;

import model.Sensor;
import model.SensorType;

import java.sql.*;  // Using 'Connection', 'Statement' and 'ResultSet' classes in java.sql package
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

public class Database {

    private static String host = "localhost";
    private static int port = 4306;
    private static String dbName = "beehive";
    private static String user = "beehive";
    private static String pass = "beehive";

    // TODO: One query to get sensordata from all sensors;
    // TODO: Prepared statements (?)
    // TODO: Set a (dynamic) limit on GET requests

    private Connection getConnection() throws SQLException {
        return DriverManager.getConnection(
                "jdbc:mysql://" + host + ":"+port+"/"+dbName,
                user, pass);   // For MySQL only
    }

    public Map<Integer, Sensor> getAllByType(SensorType type) {

        Map<Integer, Sensor> Sensors = new HashMap<>();

        try (
                Connection conn = this.getConnection();
                Statement stmt = conn.createStatement();
        ) {
            String select = "SELECT id, value, date_created FROM "+type.getTypeString();
            ResultSet result = stmt.executeQuery(select);

            int rowCount = 0;
            while (result.next()) {

                Sensor p = new Sensor(
                    result.getInt("id"),
                    type,
                    result.getFloat("value"),
                    result.getString("date_created")
                );

                Sensors.put(p.getId(), p);

                ++rowCount;
            }

        } catch (SQLException ex) {
            ex.printStackTrace();
        }

        return Sensors;
    }

    public Map<Integer, Sensor> getAllByTypeBetween(SensorType type, String timeFrom, String timeTo) {

        Map<Integer, Sensor> Sensors = new HashMap<>();

        try (
                Connection conn = this.getConnection();
                Statement stmt = conn.createStatement();
        ) {
            String select = "SELECT id, value, date_created FROM "+type.getTypeString()
                    + " WHERE date_created BETWEEN '"+timeFrom+"' AND '"+timeTo+"'";
            ResultSet result = stmt.executeQuery(select);

            while (result.next()) {

                Sensor p = new Sensor(
                    result.getInt("id"),
                    type,
                    result.getFloat("value"),
                    result.getString("date_created")
                );

                Sensors.put(p.getId(), p);
            }

        } catch (SQLException ex) {
            ex.printStackTrace();
        }

        return Sensors;
    }

    public Sensor getSensorById(SensorType type, int id) {

        Sensor Sensor = null;

        try (
                Connection conn = this.getConnection();
                Statement stmt = conn.createStatement();
        ) {
            String select = "SELECT id, value, date_created FROM "+type.getTypeString()
                    +" WHERE id = "+id; // join tables
            ResultSet result = stmt.executeQuery(select);

            while (result.next()) {

                Sensor p = new Sensor(
                        result.getInt("id"),
                        type,
                        result.getFloat("value"),
                        result.getString("date_created")
                );

                Sensor = p;
            }

        } catch (SQLException ex) {
            ex.printStackTrace();
        }

        return Sensor;
    }

    public int insertSensor(Sensor sensor) {

        var type = sensor.getType().getTypeString();
        var value = sensor.getValue();

        try (
                Connection conn = this.getConnection();
                Statement stmt = conn.createStatement();
        ) {
            stmt.executeUpdate("INSERT INTO "+type+" (value) VALUES ('"+value+"')");

            return stmt.getUpdateCount();

        } catch (SQLException ex) {
            ex.printStackTrace();
        }

        return 0;
    }
}