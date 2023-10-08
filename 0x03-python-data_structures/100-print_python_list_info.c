#include <Python.h>
#include <listobject.h>
#include <object.h>
#include <stdio.h>
/**
 * print_python_list_info -prints some basic info about Python lists.
 * @p:Pointer to the Pyobject(list)
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t size = PyList_Size(p);
	Py_ssize_t i;

	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < size; ++i)
	{
		printf("Element %zd: %s\n", i, (((PyObject *)(PyList_GetItem(p, i)))->ob_type->tp_name));
	}
}
