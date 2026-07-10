#include <Python.h>
#include <listobject.h>
#include <stdio.h>

/**
 * print_python_list_info - prints information about Python lists
 * @p: pointer to a Python object
 */
void print_python_list_info(PyObject *p)
{
    Py_ssize_t i;
    PyListObject *list;

    list = (PyListObject *)p;

    printf("[*] Size of the Python List = %ld\n", Py_SIZE(p));
    printf("[*] Allocated = %ld\n", list->allocated);

    for (i = 0; i < Py_SIZE(p); i++)
    {
        printf("Element %ld: %s\n",
               i,
               Py_TYPE(PyList_GET_ITEM(p, i))->tp_name);
    }
}
