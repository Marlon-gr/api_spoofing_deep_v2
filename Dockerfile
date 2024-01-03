
FROM atf.intranet.bb.com.br:5001/bb/lnx/lnx-python3-centos:3.6.8

ARG build_date
ARG vcs_ref
ARG VERSAO=1.0.2
ARG BOM_PATH="/docker/"

LABEL \
    br.com.bb.image.app.sigla="" \
    br.com.bb.image.app.provider="" \
    br.com.bb.image.app.arch="x86_64" \
    br.com.bb.image.app.maintainer="" \
    br.com.bb.image.app.version="$VERSAO" \
    br.com.bb.image.description="" \
    org.label-schema.maintainer="" \
    org.label-schema.vendor="" \
    org.label-schema.url="" \
    org.label-schema.name="" \
    org.label-schema.license="COPYRIGHT" \
    org.label-schema.version="$VERSAO" \
    org.label-schema.vcs-url="" \
    org.label-schema.vcs-ref="$vcs_ref" \
    org.label-schema.build-date="$build_date" \
    org.label-schema.schema-version="1.0" \
    org.label-schema.dockerfile="${BOM_PATH}/Dockerfile"

# Save Bill of Materials to image. Não remova!
COPY README.md CHANGELOG.md LICENSE Dockerfile ${BOM_PATH}/

ENV \
    VERSAO=$VERSAO

RUN mkdir -p /usr/src/spoofing_model
RUN mkdir -p /usr/src/app
COPY . /usr/src/app

RUN yum install -y gcc gcc-c++ make cmake python36-devel boost-devel libXext libSM libXrender wget

ENV CMAKE_C_COMPILER=/usr/bin/gcc CMAKE_CXX_COMPILER=/usr/bin/g++ MODE=prod

WORKDIR /usr/src/app/
RUN python3 -m pip install -U pip && pip install -e .

## Get PyTorch version 1.5.0 for Python 3.6
#RUN pip uninstall torch --yes
## hadolint ignore=DL3013
#RUN pip install torch-1.5.0-cp36-cp36m-manylinux1_x86_64.whl

EXPOSE 9000
# Save Bill of Materials to image. Não remova!
COPY README.md CHANGELOG.md LICENSE Dockerfile ${BOM_PATH}/

WORKDIR /usr/src/app/api_spoofing_deep_v2/
# Run gunicorn
ENTRYPOINT ["gunicorn", "-c", "config/config.py", "--preload", "main:app"]
