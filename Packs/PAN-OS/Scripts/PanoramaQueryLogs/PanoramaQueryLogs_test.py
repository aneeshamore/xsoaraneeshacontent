from pytest_mock import MockerFixture

def test_main(mocker: MockerFixture):
    """
    Given:
        Command args.
    When:
        Calling `main`.
    Assert:
        Ensure `execute_polling_command` is called once with the correct command name and args.
    """
    from PanoramaQueryLogs import main

    args = {
        "log-type": "threat",
        "query": "source:1.1.1.1",
        "number_of_logs": "100",
        "timeout": "120",
        "interval_in_seconds": "10"
    }
    
    mocker.patch("PanoramaQueryLogs.demisto.args", return_value=args)
    mock_execute_polling_command = mocker.patch("PanoramaQueryLogs.execute_polling_command", return_value=[])
    
    main()
    
    assert mock_execute_polling_command.call_count == 1
    assert mock_execute_polling_command.call_args[0] == ("pan-os-query-logs", args)
