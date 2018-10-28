# #! Site

This serves as the landing page for [hashbang.sh](http://hashbang.sh).

The index.html is both an html page, and a bash script, which is done by:

1.  Wrapping the html inside a bash multiline string that is ignored.
2.  Having the the bash script inside of an html comment.

This allows both bash and browsers to render this document appropriately.

## Deployment

1. Build/sign index.html (requires hashbang team private key in gpg ring)

    ```
    make
    ```

2. Build/push new docker container

    ```
    docker build -t hashbang/site .
    docker push hashbang/site
    ```
