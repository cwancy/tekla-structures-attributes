# Tekla Structures Attribute Library
A simple C# property library for using immutable attributes in Tekla Structures.

# What is the purpose
Tekla Structures Open API does not have this in-built. When getting/setting attributes using the API, it will demand a string variable to be used, which may contradict clean code architecture requirements.

To put it simply - this app "simplifies" the experience by using a reusable library instead.

As of the initial release of this code, this library contains over 780 attributes. This list is expected to grow with new releases of Tekla Structures.

# NuGet
You can install the NuGet package from here: https://www.nuget.org/packages/TeklaStructuresAttributes

# Usage
It is very simple to use. Reference the NuGet package, and use the `Attributes` class to access the large list of attribute identifiers.

## Basic Example:
Getting a property (OLD):
```cs
Part part = new Part();

string pos = "";
part.GetReportProperty("ASSEMBLY_POS", ref pos);
```

Getting a property (NEW):
```cs
Part part = new Part();

string pos = "";
part.GetReportProperty(Attributes.ASSEMBLY_POS, ref pos);
```

Whether you were storing these as a loose string, a class initialized property or something else - you don't have to anymore with this library. This library doesn't change the world, but it may be helpful when you are trying to keep your code clean of bloat.

## XML Hints
There are some XML hints that have been included. Some hints still need to be added. The main XML hint that needs pointing out is the return type. This references the return type of the property, such as the `LENGTH` attribute returning a float.

![image](https://github.com/cwancy/tekla-structures-attributes/assets/60968585/26981bb9-66f0-4e65-be94-b510c9204f7b)

# Contributing
Feel free to contribute to the issues, or create issues yourself. A goal of this project is that developers using the Tekla Open API can benefit from an easy to access library that speeds up their development process.

PR's for your own personal/organizational UDA's will be rejected, as this may be misleading to other developers.
