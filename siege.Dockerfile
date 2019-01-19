FROM archlinux/base

RUN pacman -Sy --noconfirm siege

ENTRYPOINT [ "siege" ]
