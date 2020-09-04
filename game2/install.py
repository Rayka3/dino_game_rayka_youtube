try:
    import pip
    pip.main(['install', 'pygame'])
except:
    from pip._internal import main
    main(['install', 'pygame'])
