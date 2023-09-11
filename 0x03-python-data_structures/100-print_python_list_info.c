#include <Python.h>

void print_python_list_info(PyObject *p);
/**
 * print_python_list_info - Prints basic info about Python lists
 * @p: PyObject list.
 * Return: void(empty)
 */

void print_python_list_info(PyObject *p)
{
	int size, i, allocate;
	PyObject *object;

	size = Py_SIZE(p);
	allocate = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", allocate);

	for (i = 0; i < size; i++)
	{
		printf("Element %d: ", i);

		object = PyList_GetItem(p, i);
		printf("%s\n", Py_TYPE(object)->tp_name);
	}
}
