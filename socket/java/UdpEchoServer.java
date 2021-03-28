package socket.java;

import java.net.DatagramSocket;

public class UdpEchoServer {
    static int PORT = 8322;
    public static void main(String[] args) {
        UdpSock s = null;
        try {
            s = new UdpSock(new DatagramSocket(PORT), true);
            while (true) {
                String[] r = s.recv();
                String host = r[1].split(":")[0].substring(1);
                int port = Integer.parseInt(r[1].split(":")[1]);
                s.send(r[0], host, port);
            }
        } catch (Exception e) { e.printStackTrace(); }
        finally {
            if (s != null)
                s.close();
        }
    }
}
