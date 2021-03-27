package socket.java;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;

/**
 * tcp socket wrapper
 * easy to send/recv(no concerned about stream)
 * provide log feature, input from stdin
 */
public class TcpSock {
    Socket sock = null;
    String host = null;
    int port = 0;
    PrintWriter pw = null;
    BufferedReader br = null;
    boolean log = false;
    BufferedReader stdin = null;

    /**
     * create socket and connect
     * @param host remote host
     * @param port remote port
     * @param log (Optional) whether print log. default true
     * @throws IOException
     */
    public TcpSock(String host, int port, boolean log) throws IOException {
        sock = new Socket(host, port);
        this.host = host;
        this.port = port;
        this.log = log;
    }
    public TcpSock(String host, int port) throws IOException {
        this(host, port, true);
    }
    /**
     * copy creator
     * @param s socket to be copied
     * @param log (Optional) whether print log. default true
     */
    public TcpSock(Socket s, boolean log) {
        sock = s;
        host = s.getInetAddress().getHostAddress();
        port = s.getLocalPort();
        this.log = log;
    }
    public TcpSock(Socket s) {
        this(s, true);
    }

    /**
     * send msg
     * @param msg message
     * @throws IOException
     */
    public void send(String msg) throws IOException {
        if (pw == null)
            pw = new PrintWriter(sock.getOutputStream(), true);
        pw.print(msg);
        pw.flush();
        if (log)
            System.out.println("[*] Send: " + msg);
    }

    /**
     * recv line and return
     * @return one received line(doesn't contain '\n')
     * @throws IOException
     */
    public String recvLine() throws IOException {
        if (br == null)
            br = new BufferedReader(new InputStreamReader(sock.getInputStream()));
        String data = br.readLine();
        if (log)
            System.out.println("[*] Recv: " + data);
        return data;
    }

    /**
     * close socket, streams
     * @throws IOException
     */
    public void closeAll() throws IOException {
        if (sock != null)
            sock.close();
        if (pw != null)
            pw.close();
        if (br != null)
            br.close();
        if (stdin != null)
            stdin.close();
        if (log)
            System.out.println("[*] socket, streams are closed");
    }

    /**
     * equivalent to python input()
     * @param prompt
     * @return doesn't contain '\n'
     * @throws IOException
     */
    public String input(String prompt) throws IOException {
        if (stdin == null)
            stdin = new BufferedReader(new InputStreamReader(System.in));
        System.out.print(prompt);
        return stdin.readLine();
    }
}
