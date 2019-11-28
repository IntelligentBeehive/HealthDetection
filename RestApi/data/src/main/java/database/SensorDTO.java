package database;

public class SensorDTO {
    private int id;
    private String name;
    private String password;
    private int score;
    private int gamesPlayed;

    public SensorDTO(String name, String password) {
        this.name = name;
        this.password = password;
    }

    public SensorDTO(int id, String name, int score, int gamesPlayed) {
        this.id = id;
        this.name = name;
        this.score = score;
        this.gamesPlayed = gamesPlayed;
    }

    public int getId() {
        return id;
    }

    public String getName() {
        return name;
    }

    public String getPassword() {
        return password;
    }

    public int getScore() {
        return score;
    }

    public int getGamesPlayed() {
        return gamesPlayed;
    }

    @Override
    public String toString() {
        return "Sensor: "+ this.name +"; Score: "+score+"; Games Played: "+gamesPlayed+";";
    }
}