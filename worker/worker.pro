TEMPLATE = lib
CONFIG += console c++11
CONFIG -= app_bundle
CONFIG -= qt

INCLUDEPATH += /usr/local/include
LIBS += -L/usr/local/lib -lnanomsg

SOURCES += \
    worker.cpp

HEADERS += \
    worker.h
