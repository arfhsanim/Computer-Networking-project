import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.*;
public class Get {
public static void main(String[] args) throws MalformedURLException,
IOException {
URL wp_Url = new URL("http://webcode.me"); // Create an instance of the URL
//class with the url of the web page
// in the constructor.

HttpURLConnection httpURLCon = (HttpURLConnection)
wp_Url.openConnection();

// Create an instance of the
// HTTPURLConnection class, return from
// the functionopenConnection()

httpURLCon.setRequestMethod("GET");
// Enable the HTTP method using setRequestMethod() function,
//the parameteris“GET”
int responseCo = httpURLCon.getResponseCode();
if (responseCo == HttpURLConnection.HTTP_OK) { // HTTP_OK = 200
System.out.println("\nThe response massage from website is:"+

httpURLCon.getResponseMessage()

+ "-" + httpURLCon.getResponseCode() + "\n");
InputStreamReader inp = new
InputStreamReader(httpURLCon.getInputStream());

BufferedReader buff = new BufferedReader(inp);
StringBuffer respo = new StringBuffer();
String inpLine = null;
{
while ((inpLine = buff.readLine()) != null) {
respo.append(inpLine);
respo.append(System.lineSeparator());
}
buff.close();
System.out.print("The website is:\n\n" + respo);
}
}
}
}