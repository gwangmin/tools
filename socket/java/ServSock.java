package socket.java;

import java.io.IOException;
import java.net.ServerSocket;

/**
 * tcp server socket wrapper
 * accept method return TcpSock obj
 * provide log feature
 */
public class ServSock {
    ServerSocket sock = null;
    int port = 0;
    boolean log = false;

    /**
     * create server socket
     * @param port local port
     * @param log (Optional) whether print log. default true
     * @throws IOException
     */
    public ServSock(int port, boolean log) throws IOException {
        sock = new ServerSocket(port);
        this.port = port;
        this.log = log;
        if (log)
            System.out.println("[*] Server opened at " + port);
    }
    public ServSock(int port) throws IOException {
        this(port, true);
    }
    /**
     * copy creator
     * @param s socket to be copied
     * @param log (Optional) whether print log. default true
     * @throws IOException
     */
    public ServSock(ServerSocket s, boolean log) {
        sock = s;
        port = s.getLocalPort();
        this.log = log;
        if (log)
            System.out.println("[*] Server opened at " + port);
    }
    public ServSock(ServerSocket s) {
        this(s, true);
    }

    /**
     * equivalent to serversocket.accept but it wraps TcpSock
     * @return TcpSock obj with this.log
     * @throws IOException
     */
    public TcpSock accept() throws IOException {
        TcpSock s = new TcpSock(sock.accept(), log);
        if (log)
            System.out.println("[*] Connected: " + s.host + ":" + s.port);
        return s;
    }

    /**
     * close server
     * @throws IOException
     */
    public void close() throws IOException {
        if (sock != null)
            sock.close();
    }
}
