# Stage 1: Build container image
FROM alpine as cmatrixbuilder

WORKDIR cmatrix

RUN apk update --no-cache && \
    apk add git autoconf automake alpine-sdk ncurses-dev ncurses-static  && \
    git clone https://github.com/spurin/cmatrix.git .  && \
    autoreconf -i  && \
    mkdir -p /usr/lib/consolefonts /usr/share/consolefonts && \
    ./configure LDFLAGS="-static"  && \
    make


# Stage 2: cmatrix Container Image
FROM alpine

LABEL org.opencontainers.image.authors="Khoa Nguyen" \
      org.opencontainers.image.description="Container Image for https://github.com/abishekvashok/cmatrix"

RUN apk update --no-cache && \
    apk add ncurses-terminfo-base && \
    adduser -g "Khoa Nguyen" -s /usr/sbin/nologin -D -H khoaguin  

COPY --from=cmatrixbuilder /cmatrix/cmatrix /cmatrix

USER khoaguin

ENTRYPOINT ["./cmatrix"]
CMD ["-b"]

