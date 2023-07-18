#include <Python.h>
#include <object.h>
#include <listobject.h>
void print_python_list_info(PyObject *p)
{
	int i;
	long int size = PyList_Size(p);
	PyListObject *object = (PyListObject *)p;
	printf("[*] Size of the Python List = %li\n", size);
	printf("[*] Allocated = %li\n", object->allocated);
	for (i = 0; i < size; i++)
		printf("Element %i: %s\n", i, Py_TYPE(object->ob_item[i])->tp_name);
}
