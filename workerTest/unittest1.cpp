#include "stdafx.h"
#include "CppUnitTest.h"
#include <string>

using namespace Microsoft::VisualStudio::CppUnitTestFramework;

namespace workerTest
{		
	TEST_CLASS(UnitTest1)
	{
	public:
		
		TEST_METHOD(TestWorker)
		{
			worker("worker1");
		}

	};
}