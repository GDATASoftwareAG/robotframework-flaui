$Source = @"
using System.Net;

public class ExtendedWebClient : WebClient {
    public int Timeout;

    protected override WebRequest GetWebRequest(System.Uri address) {
        WebRequest request = base.GetWebRequest(address);
        if (request != null) {
            request.Timeout = Timeout;
        }
        return request;
    }

    public ExtendedWebClient() {
        Timeout = 100000;
    }
}
"@;

Add-Type -TypeDefinition $Source -Language CSharp

$webClient = New-Object ExtendedWebClient;
$webClient.Timeout = 300000;
$webClient.UploadFile("https://ci.appveyor.com/api/testresults/junit/$($env:APPVEYOR_JOB_ID)", (Resolve-Path .\result\xunit.xml))
