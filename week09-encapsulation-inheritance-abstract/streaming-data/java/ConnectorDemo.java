import java.time.Instant;
import java.time.LocalDateTime;
import java.time.ZoneOffset;
import java.util.List;

/*
 * Connectors, Java style. Compare with connectors/base.py and sources.py.
 * Run (Java 16+):  java ConnectorDemo.java
 *
 * What Java makes you write that Python lets you skip:
 *   - "super(...)" in SpotifyConnector; "@Override" is checked by the compiler
 *   - types required everywhere: a variable has a declared type AND an actual type
 *   - "private final" / "protected": the compiler, not a convention, enforces visibility
 *   - "record": an immutable data carrier, like a NamedTuple or a frozen dataclass
 */
public class ConnectorDemo {
    public static void main(String[] args) {
        // Declared type: Connector.  Actual type: SpotifyConnector.
        Connector c = new SpotifyConnector(List.of("2024-09-02T13:00:00Z,180000,Neon Harbor"));
        System.out.println(c.load());   // the Spotify version of load() runs, due to actual type, determined at runtime

        List<Connector> sources = List.of(
            c,
            new NetflixConnector(List.of("2024-09-03 01:15:22,2710,Harbor Lights"))
        );
        System.out.printf("Total hours: %.3f%n", totalHours(sources));  
        // never asks which class. 

        StreamingClient client = new StreamingClient("ana", "s3cr3t-token-123");
        System.out.println(client);          // the token is not in the output
        // System.out.println(client.token); // compile error: token has private access
    }

    /** Works for ANY Connector: it only knows the declared type. 
     * At runtime, when a method is invoked on a source, the actual type of the object
     * is used to invoke the appropriate method.
    */
    static double totalHours(List<Connector> sources) {
        double seconds = 0.0;
        for (Connector source : sources) {
            for (StreamingSession session : source.load()) {
                seconds += session.seconds();
            }
        }
        return seconds / 3600.0;
    }
}

/** An immutable record. */
record StreamingSession(Instant when, String title, double seconds, String source) {}

/** The base class: subclasses specialise it. */
class Connector {
    protected final List<String> lines;  // visible to subclasses, hidden from everyone else

    Connector(List<String> lines) {
        this.lines = List.copyOf(lines);  // defensive copy: callers cannot change us later
    }

    String name() {
        return getClass().getSimpleName().replace("Connector", "").toLowerCase();
    }

    List<StreamingSession> load() {
        throw new UnsupportedOperationException(getClass().getSimpleName() + " must override load()");
    }
}

class SpotifyConnector extends Connector {   // "ISO timestamp,ms_played,title"
    SpotifyConnector(List<String> lines) {
        super(lines);
    }

    @Override
    List<StreamingSession> load() {
        return lines.stream().map(line -> {
            String[] parts = line.split(",", 3);
            return new StreamingSession(Instant.parse(parts[0]), parts[2], Long.parseLong(parts[1]) / 1000.0, name());
        }).toList();
    }
}

class NetflixConnector extends Connector {   // "start time,seconds,title"
    NetflixConnector(List<String> lines) {
        super(lines);
    }

    @Override
    List<StreamingSession> load() {
        return lines.stream().map(line -> {
            String[] parts = line.split(",", 3);
            Instant when = LocalDateTime.parse(parts[0].replace(' ', 'T')).toInstant(ZoneOffset.UTC);
            return new StreamingSession(when, parts[2], Double.parseDouble(parts[1]), name());
        }).toList();
    }
}

class StreamingClient {
    private final String username;
    private final String token;

    StreamingClient(String username, String token) {
        this.username = username;
        this.token = token;
    }

    @Override
    public String toString() {
        return "StreamingClient(username=" + username + ", token=***)";
    }
}
