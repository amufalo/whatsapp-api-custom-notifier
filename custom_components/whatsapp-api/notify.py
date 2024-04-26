import logging
import voluptuous as vol
import requests
import homeassistant.helpers.config_validation as cv
from homeassistant.components.notify import (
    ATTR_TARGET, PLATFORM_SCHEMA, BaseNotificationService)

CONF_URL = 'url'
CONFIG_TOKEN = 'token'
_LOGGER = logging.getLogger(__name__)

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Required(CONF_URL): cv.string,
    vol.Optional(CONFIG_TOKEN): cv.string,
}, extra=vol.ALLOW_EXTRA)

def get_service(hass, config, discovery_info=None):
    """Get the custom notifier service."""
    url = config.get(CONF_URL)
    token = config.get(CONFIG_TOKEN)
    return WhatsappApiNotificationService(url,token)

class WhatsappApiNotificationService(BaseNotificationService):
    def __init__(self, url, token=None):
        self._url = url
        self.token = token
        
    def send_message(self, message="", **kwargs):
        chatid = kwargs.get(ATTR_TARGET)

        data = {
            
            "content": message,
            "contentType": "string",
            "chatId": chatid
        }
        try:
            if self.token is None:
                headers = {}
            else:
                headers = {"Authorization": "Bearer " + self.token} 
            response = requests.post(self._url, json=data,headers = headers)
            _LOGGER.info("Message sent")
            response.raise_for_status()
        except requests.exceptions.RequestException as ex:
            _LOGGER.error("Error sending notification using whatsapp-api: %s", ex)