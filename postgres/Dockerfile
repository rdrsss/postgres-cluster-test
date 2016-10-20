FROM ubuntu:14.04

# Install wget
RUN \
	apt-get update -q &&\
	DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends apt-utils &&\
	DEBIAN_FRONTEND=noninteractive apt-get install -y wget

# Add postgres to apt source
RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ trusty-pgdg main" | tee --append /etc/apt/sources.list.d/pgdg.list

# Import key
RUN \
	wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | \
	apt-key add -

# Update apt and Install
RUN \
	apt-get update -qq &&\
	DEBIAN_FRONTEND=noninteractive apt-get install -y postgresql

# Set path
ENV PATH /usr/lib/postgresql/9.6/bin:$PATH
ENV PGDATA /var/lib/postgresql/data
# TODO : Setup some volume thing
VOLUME /var/lib/postgresql/data

EXPOSE 5432

# Create user to run 
#RUN useradd -ms /bin/bash postgres
RUN adduser postgres sudo

USER postgres
CMD ["postgres"]
