import ask_sdk_core
from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler, AbstractExceptionHandler
from ask_sdk_core.utils import is_request_type, is_intent_name
sb = SkillBuilder()

class ErrorHandler(AbstractExceptionHandler):
    def can_handle(self, handler_input, exception):
        return True

    def handle(self, handler_input, exception):
        speech_text = 'Sorry, your skill encountered an error';
        print(exception)
        handler_input.response_builder.speak(speech_text).set_should_end_session(False)
        return handler_input.response_builder.response

class LaunchRequestHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return is_request_type("LaunchRequest")(handler_input)
    
    def handle(self, handler_input):
        speech_text = 'What Do you want to know';
        handler_input.response_builder.speak(speech_text).set_should_end_session(False)
        return handler_input.response_builder.response

class GetTheDayMoodHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return is_intent_name("GetTheDayMood")(handler_input)

    def handle(self, handler_input):
        #slotValue = handler_input.request_envelope.request.intent.slots['slotName'].value
        speech_text = "Today is a bit rainy but definitely a good day";
        handler_input.response_builder.speak(speech_text).set_should_end_session(False)
        return handler_input.response_builder.response


sb.add_exception_handler(ErrorHandler())
#delete undefined built-in intent handlers
sb.add_request_handler(LaunchRequestHandler())
#add custom request handlers
sb.add_request_handler(GetTheDayMoodHandler())

def handler(event, context):
    return sb.lambda_handler()(event, context)
