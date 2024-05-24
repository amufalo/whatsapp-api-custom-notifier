# whatsapp-api-custom-notifier

- We will use the  https://github.com/chrishubert/whatsapp-api/ repository to run a container into docker.
```bash
docker run -v /docker/sessions:/usr/src/app/sessions \
       --name whatsapp_web_api \
       -p 3000:3000 \
       -e API_KEY=your_api_key \
       -e BASE_WEBHOOK_URL=http://localhost:3000/localCallbackExample \
       -e ENABLE_LOCAL_CALLBACK_EXAMPLE=TRUE \
       -e MAX_ATTACHMENT_SIZE=5000000 \
       -e SET_MESSAGES_AS_SEEN=TRUE \
       -e DISABLED_CALLBACKS="message_ack|message_reaction" \
       -e ENABLE_SWAGGER_ENDPOINT=TRUE \
       chrishubert/whatsapp-web-api:latest
```

- Navigate to http://url_from_whatsapp-api/session/start/your_session to start your session. Scan QR Code generated in docker logs.

configuration.yaml:
```yaml
notify:
  - platform: whatsapp-api
    name: whatsapp
    url: http://url_from_whatsapp-api/client/sendMessage/your_session
    token: your_api_key
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
