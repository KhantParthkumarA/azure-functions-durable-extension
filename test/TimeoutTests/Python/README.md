To repro timeout in entity function,
call

curl http://localhost:7071/api/start/EntityTimeout1

The desired behavior is that when the entity operation times out, a failure response is sent to the orchestrator which then catches the exception and terminates successfully.

(For reference, see the C# version in test\TimeoutTests\CSharp\EntityTimeout.cs)
