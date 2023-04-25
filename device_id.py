import json
import uuid

def send_telemetry(device_client, data):
    # Create a unique message ID
    message_id = str(uuid.uuid4())
    
    # Add message ID and device ID to telemetry data
    telemetry_data = {"messageId": message_id, "deviceId": device_client._client_id,
                      "temperature": data["temperature"], "humidity": data["humidity"]}
    
    # Convert telemetry data to JSON string
    message = Message(json.dumps(telemetry_data))
    
    # Send telemetry message to IoT Hub
    device_client.send_message(message)
    
    print(f"Sent telemetry: {telemetry_data}")
