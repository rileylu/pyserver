#pragma once
#include <string>
#ifdef _WIN32
#define API __declspec(dllexport)
#else
#define API
#endif

void API worker(const std::string& name);
