package socket.java;

import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;
import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.io.IOException;
import java.net.SocketException;
import java.net.UnknownHostException;

/**
 * udp socket wrapper
 * easy to send/recv(no concerned about DatagramPacket)
 * provide log feature, input from stdin
 */
public class UdpSock {
    DatagramSocket sock = null;
    boolean log = false;
    BufferedReader stdin = null;

    /**
     * create udp socket
     * @param log (Optional) whether print log. default true
     * @throws SocketException
     */
    public UdpSock(boolean log) throws SocketException {
        sock = new DatagramSocket();
        this.log = log;
    }
    public UdpSock() throws SocketException {
        this(true);
    }
    /**
     * copy creator
     * @param s socket to be copied
     * @param log (Optional) whether print log. default true
     */
    public UdpSock(DatagramSocket s, boolean log) {
        sock = s;
        this.log = log;
    }
    public UdpSock(DatagramSocket s) {
        this(s, true);
    }
    
    /**
     * send msg by udp
     * @param msg message
     * @param hostName remote host
     * @param port remote port
     * @throws UnknownHostException
     * @throws IOException
     */
    public void send(String msg, String hostName, int port) throws UnknownHostException, IOException {
        InetAddress addr = InetAddress.getByName(hostName);
        byte buf[] = msg.getBytes();
        DatagramPacket dp = new DatagramPacket(buf, buf.length, addr, port);
        sock.send(dp);
        if (log)
            System.out.println("[*] Sendto: " + msg + "; " + hostName + ":" + port);
    }
    
    /**
     * receive and return {msg, addr}
     * @param bufsize (Optional) receiving packet size. default 1024
     * @return string message, addr string
     * @throws IOException
     */
    public String[] recv(int bufsize) throws IOException {
        // receive
        byte buf[] = new byte[bufsize];
        DatagramPacket dp = new DatagramPacket(buf, buf.length);
        sock.receive(dp);

        // return
        String data = new String(dp.getData());
        String addr = dp.getAddress() + ":" + dp.getPort();
        if (log)
            System.out.println("[*] Recvfrom: " + data + "; " + addr);
        return new String[]{data, addr};
    }
    public String[] recv() throws IOException {
        return recv(1024);
    }
    /**
     * close socket
     */
    public void close() {
        if (sock != null)
            sock.close();
    }

    /**
     * equivalent to python input()
     * @param prompt
     * @return
     * @throws IOException
     */
    public String input(String prompt) throws IOException {
        if (stdin == null)
            stdin = new BufferedReader(new InputStreamReader(System.in));
        System.out.print(prompt);
        return stdin.readLine();
    }
}
