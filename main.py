from website import create_app

app = create_app()

if __name__ == '__main__':
    # remove debug for production
    app.run(host='0.0.0.0', debug=True)