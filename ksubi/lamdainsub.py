import ask_sdk_core
from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler, AbstractExceptionHandler
from ask_sdk_core.utils import is_request_type, is_intent_name

def handler(event, context):
    sb = SkillBuilder()
    
    sb.add_exception_handler(ErrorHandler())
    #delete undefined built-in intent handlers
    sb.add_request_handler(CancelIntentHandler())
    sb.add_request_handler(HelpIntentHandler())
    sb.add_request_handler(StopIntentHandler())
    sb.add_request_handler(NavigateHomeIntentHandler())
    sb.add_request_handler(FallbackIntentHandler())
    sb.add_request_handler(LaunchRequestHandler())
    sb.add_request_handler(SessionEndedRequestHandler())
    #add custom request handlers
    #sb.add_request_handler(CustomIntentHandler())
    
    def handler(event, context):
        return sb.lambda_handler()(event, context)
    print("Test")
    return {"message": "Successfully executed"}
