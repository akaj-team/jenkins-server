taskkill /F /IM IEDriverServer.exe /T
taskkill /F /IM MicrosoftWebDriver.exe /T
taskkill /F /IM operadriver.exe /T
java -jar selenium-server-standalone-3.141.59.jar -nodeConfig nodeConfig.json -role node
pause