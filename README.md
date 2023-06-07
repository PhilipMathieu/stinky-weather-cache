This repo is a minimal implementation of a GitHub Pages site that periodically queries a JSON API and stores the most recent successful query. This is intended to be used as a layer of redundancy for systems that use unreliable APIs.

## Configuration

1. Update the request URL by editing `config.json`
2. Change the update frequency by editing the cron timing in `./github/workflows/python-app.yml`
3. Enable GitHub Pages in the repository settings

## Known Limitations

- This currently only works for applications where the response is of type `application/json; utf-8`
