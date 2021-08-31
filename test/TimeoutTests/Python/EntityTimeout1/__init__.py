# This function is not intended to be invoked directly. Instead it will be
# triggered by an HTTP starter function.
# Before running this sample, please:
# - create a Durable activity function (default name is "Hello")
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

import logging
import json

import azure.functions as func
import azure.durable_functions as df

def orchestrator_function(context: df.DurableOrchestrationContext):
    entityId = df.EntityId("SlowEntity", context.instance_id)
    try:
        current_value = yield context.call_entity(entityId, "", 180)
        return "test failed: expected exception, but no exception thrown"
    except:
        return "test passed: exception thrown"

main = df.Orchestrator.create(orchestrator_function)