#include <Arduino.h>
#include <Notecard.h>

using namespace blues;
#define message  "hello world"
#define usbSerial Serial
#define productUID "com.elithecomputerguy.eli:iot_demo"

Notecard notecard;

// the setup function runs once when you press reset or power the board
void setup()
{
  delay(2500);
  usbSerial.begin(115200);
  notecard.begin();
  notecard.setDebugOutputStream(usbSerial);

  J *req = notecard.newRequest("hub.set");
  JAddStringToObject(req, "product", productUID);
  JAddStringToObject(req, "mode", "continuous");
  JAddStringToObject(req, "mode", "continuous");

  notecard.sendRequest(req);
}

void loop()
{
  J *req = notecard.newRequest("note.add");
  if (req != NULL)
  {
    JAddStringToObject(req, "file", "sensors.qo");
    JAddBoolToObject(req, "sync", true);
    J *body = JAddObjectToObject(req, "body");
    if (body)
    {
      JAddStringToObject(body, "message", message);
    }
    notecard.sendRequest(req);
  }

  delay(300000);
}