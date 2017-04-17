TEMPLATE = app
CONFIG += console c++11
CONFIG -= app_bundle
CONFIG -= qt

SOURCES += main.cpp

unix:!macx: LIBS += -L$$PWD/reqrep_device/debug/ -lreqrep_device

INCLUDEPATH += $$PWD/reqrep_device
DEPENDPATH += $$PWD/reqrep_device

unix:!macx: LIBS += -L$$PWD/worker/debug/ -lworker

INCLUDEPATH += $$PWD/worker
DEPENDPATH += $$PWD/worker

LIBS += -lpthread
