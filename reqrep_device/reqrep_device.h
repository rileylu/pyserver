#pragma once

#ifdef _WIN32
#define API __declspec(dllexport)
#else
#define API
#endif

void API reqrep_device();
