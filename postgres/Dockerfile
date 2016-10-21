FROM ubuntu:14.04

# Container env var, no tty
ENV DEBIAN_FRONTEND=noninteractive
# Set locale 
#ENV LC_ALL en_US.UTF-8
RUN locale-gen "en_US.UTF-8"

# Install wget
RUN \
	apt-get update -q &&\
	apt-get install -y --no-install-recommends apt-utils &&\
	apt-get install -y wget

# Avoid ERROR: invoke-rc.d: policy-rc.d denied execution of start.
RUN echo "#!/bin/sh\nexit 0" > /usr/sbin/policy-rc.d

# Add postgres to apt source
RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ trusty-pgdg main" | tee --append /etc/apt/sources.list.d/pgdg.list

# Import key
RUN \
	wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | \
	apt-key add -

# Update apt and Install
RUN \
	apt-get update -qq &&\
	apt-get install -y postgresql postgresql-contrib

# Set path
ENV PATH /usr/lib/postgresql/9.6/bin:$PATH
ENV PGDATA /var/lib/postgresql/data
# TODO : Setup some volume thing
VOLUME /var/lib/postgresql/data

# Expose port
EXPOSE 5432

# Add postgres server config
ADD postgresql.conf /var/lib/postgresql/data/

# Create user to run 
#RUN useradd -ms /bin/bash postgres
RUN adduser postgres sudo

USER postgres
CMD ["postgres"]
