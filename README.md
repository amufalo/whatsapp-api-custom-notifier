# whatsapp-api-custom-notifier

- Install https://github.com/chrishubert/whatsapp-api/
- Navigate to http://url_from_whatsapp-api/session/start/your_session to start your session. Scan QR Code generated in docker logs.

configuration.yaml:
```yaml
notify:
  - platform: whatsapp-api
    name: whatsapp
    url: http://url_from_whatsapp-api/client/sendMessage/your_session
    token: x
```

Example of use:
```yaml
service: notify.whatsapp
data:
  message: "{{ trigger.event.data.item.name }}"
  target: chatid
```

How to obtain chat_id?
```bash
curl http://url_from_whatsapp-api/client/getContacts/your_session
```
